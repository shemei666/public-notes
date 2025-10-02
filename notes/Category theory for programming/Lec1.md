```haskell
class Monoid m where
	mempty :: m
	mappend :: m -> m -> m
```

```haskell
instance Monoid String where
	mempty = ""
	mappend = (++)
```

# Kleisli Categories

We have seen how to model pure functions and types as categories. To model functions that are not pure i.e. having some side effect. Lets look at functions that log.
```cpp
string logger;

bool negate(bool b) {
     logger += "Not so! ";
     return !b;
}
```
We can make this a pure function by passing in and out the log.
```cpp
pair<bool, string> negate(bool b, string logger) {
     return make_pair(!b, logger + "Not so! ");
}
```

But is there a way to do the same thing less intrusively? 
```cpp
pair<bool, string> negate(bool b) {
     return make_pair(!b, "Not so! ");
}
```
The idea is that the log can be aggregated between function calls

Lets switch to a more realistic example:
```cpp
string toUpper(string s) {
    string result;
    int (*toupperp)(int) = &toupper; // toupper is overloaded
    transform(begin(s), end(s), back_inserter(result), toupperp);
    return result;
}
```

```cpp
vector<string> toWords(string s) {
    return words(s);
}
```
We can create a template `Writer` to do this
```cpp
template<class A>
using Writer = pair<A, string>;
```

```cpp
Writer<string> toUpper(string s) {
    string result;
    int (*toupperp)(int) = &toupper;
    transform(begin(s), end(s), back_inserter(result), toupperp);
    return make_pair(result, "toUpper ");
}

Writer<vector<string>> toWords(string s) {
    return make_pair(words(s), "toWords ");
}
```

```cpp
Writer<vector<string>> process(string s) {
    auto p1 = toUpper(s);
    auto p2 = toWords(p1.first);
    return make_pair(p2.first, p1.second + p2.second);
}
```

But this is also tedious, but we can abstract it.
The same code in Haskell is given below:
```haskell
import Data.Char (toUpper)
type Writer a = (a, String)

-- morphisms are from arbitrary type to Writer type

(>=>) :: (a -> Writer b) -> (b -> Writer c) -> (a -> Writer c)

m1 >=> m2 = \x ->
  let (y, s1) = m1 x
      (z, s2) = m2 y
   in (z, s1 ++ s2)

-- we have as our identity function as

return :: a -> Writer a
return x = (x, "")
  
upCase :: String -> Writer String
upCase s = (map toUpper s, "upCase ")

toWords :: String -> Writer [String]
toWords s = (words s, "toWords ")

process :: String -> Writer [String]
process = upCase >=> toWords
```

 Morphisms from type A to type B are functions that go from A to a type derived from B using the particular embellishment. The imprecise term “embellishment” corresponds to the notion of an endofunctor in a category.

## Initial Object
The **initial object** is the object with one and only one morphism going to any object in the category

This gives us uniqueness up to isomorphism. The initial object of a poset is called its least element. But not all posets may have initial objects. eg:$\mathbb{Z}$

In the category $\mathbf{Set}$, $\{  \}$ is the initial object, corresponding to `{haskell} Void` in Haskell.
The unique polymorphic function from `{haskell} Void` to any other type is called `{haskell} absurd`:
```haskell
absurd :: Void -> a
```

## Terminal Object
The **Terminal object** is the object with one and only one morphism coming to it from any object in the category

In a poset this would be the maximal object if it exists.
In $\mathbf{Set}$  it would be any singleton. denoted by the unit type `()` in Haskell.

## Duality
**Def:**$\mathscr{C}^{op}$ is the opposite category made from the category $\mathscr{C}$ by reversing all the arrows in the category.

## Products
We know how to take products in sets but how do we generalize it for other categories. We have 2 functions associated with the product.
```haskell
fst :: (a,b) -> a
fst (x,y) = x

snd :: (a,b) -> a
snd (x,y) = y
```

This pattern can be seen as
![[Pasted image 20250709200317.png]]
There might be more than one candidate for c.
Let as take `Int` and `Bool` as  the constituents of the product. Then what is a possible candidate for c? a choice is `Int` itself
```haskell
p :: Int -> Int
p x = x

q :: Int -> Bool
q _ = True 
```
Or even `{haskell} (Int,Int,Bool)` can be one
```haskell
p :: (Int,Int,Bool) -> Int
p (x,_,_) = x

q :: (Int,Int,Bool) -> Bool
q (_,_,b) = b
```

We want to be able to compare 2 instances of our pattern. We would like to say that c is "better" than c' if there is a morphism from c' to c and the projections p' and q' can be made from p , q and the morphism m.
![[Pasted image 20250709201029.png]]

another way of looking at it is that m _factorizes_ p' and q'

**Def:** A product of 2 objects a and b is the object c equipped with 2 projections such that for any other object c' equipped with 2 projections there is a unique morphism m from c' to c that factorizes those projections.

## Coproduct
#todo

## Challenges
![[Pasted image 20250710002455.png]]


## Functors in Programming

#### The maybe functor
`data Maybe a = Nothing | Just a`
Maybe itself is not a type, it is a type constructor. It takes a type a and turns it into a type Maybe a. Can we turn this into a functor?

So given a f:: a-> b we would like to produce a function Maybe a -> maybe b
```haskell
f' :: Maybe a -> Maybe b
f' Nothing = Nothing
f' (Just x) = Just (f x)
```

the morphism map can be written as
```haskell
fmap :: (a-> b) -> (Maybe a -> Maybe b)
-- or
fmap :: (a->b) -> Maybe a -> Maybe b
fmap _ Nothing = Nothing
fmap f (Just x) = Just (f x)
```

To prove this we use equational reasoning, the function definitions in Haskell are always defined as equalities. So the pattern on the left side can be replaced with the one on the right or vice-versa.

```haskell
fmap id Nothing
= Nothing
= id Nothing

fmap id (Just x)
=Just (id x)
= Just x
= id (Just x)
```
Hence identity is preserved

Now for composition
```haskell
fmap (g.f) Nothing
= Nothing
= fmap g Nothing
= fmap g (fmap f Nothing)

fmap (g.f) (Just x)
= Just (g.f x)
= Just (g (f x))
= fmap g (Just (f x))
= fmap g (fmap f (Just x))
(fmap g . fmap f) (Just x)
```

## List Functor
```haskell
instance Functor List where
	fmap _ Nil = Nil
	fmap f (Cons x t) = Cons (f x) (fmap f t)
```

## The Reader Functor
In Haskell a function type is constructed by the arrow type constructor
```haskell
a -> b
(->) a b
```

```haskell
instance Functor ((->) r) where
	fmap f g = f . g
```
## Functors as Containers
#todo 
## Composing Functors
#todo 
