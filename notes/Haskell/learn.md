#### Type variables
checking the type of the head function we get
```
1. ghci> :t head  
2. head :: [a] -> a
```
here a is a type variable. That means that a can be of any type. These are called polymorphic functions

#### Typeclasses 101
A typeclass is a sort of interface that defines some behavior. if a type is a part of a typeclass that mean it implements some behavior dictated by the typeclass. 
```haskell
 ghci> :t (==)  
 (==) :: (Eq a) => a -> a -> Bool
```
We see a `{haskell} =>` symbol here. Everything before => is called a class constraint.
The statement means the == function takes any two values that are of the same type a and returns a Bool and these types must be members of the Eq class( class constraint.)

`Eq` typeclass provides an interface for testing for equality. Any type where we can possibly check for equality should be a member of this class.

Some basic typeclasses:
`Eq` : for equality checking
`Ord` : for type with an ordering. Ord covers all the standard comparing functions like < > <= >= 
The `compare` function takes 2 Ord members of the same type and return an Ordering, it is a type that can be GT, LT, EQ

To be a member of Ord, a type must first have membership in the Eq class

`Show`: Members of this class can be presented as strings. using the function `show` we can take in a value whose type is in the `Show` class and present it as a string.

`Read` : `read` function takes in a string and returns a type which is a member of Read

`Enum`:members are sequentially ordered types. can use `succ` and `pred` functions. types: `(),Bool,Char,Ordering,Int,Integer,Float,Double`

`Bounded`: members have an upper and lower bound
`minBound` and `maxBound` have type `(Bounded a) => a`. In a sense they are polymorphic constants.

`Num` : Numeric typeclass. number in Haskell are polymorphic constants.

`Integral`: Contains only integral numbers
`Floating`: Contains only floating point numbers

### Syntax in Functions
#### Pattern Matching
When defining functions, we can define separate bodies for different patterns. This leads to easily readable code

```haskell
lucky :: (Integral a) => a -> String
lucky 7 = "LUCKY NUMBER SEVEN"
lucky x = "Sorry"
```

```haskell
factorial :: (Integral a) => a -> a
factorial 0 = 1
factorial n = n * factorial (n-1)
```

```haskell
addVectors (x1,y1) (x2,y2) = (x1+x2,y1+y2)
```

an example of head
```haskell
head' :: [a] -> a  
head' [] = error "Can't call head on an empty list, dummy!"  
head' (x:_) = x
```

We can use `@` to keep a reference to the whole object like shown below
```haskell
capital :: String -> String
capital "" = "Empty"
capital all@(x:xs) = "The first letter of " ++ all ++ " is " ++ [x]
```

### Guards
```haskell
densityTell :: (RealFloat a) => a -> String
densityTell density
	| density < 1.2 = "Float in the sky"
	| density <= 1000.0 = "Float in the sea"
	| otherwise = "Sink"
```


```haskell
max' :: (Ord a) => a -> a -> a
max' a b
	| a > b = a
	| otherwise = b
```

### Case Expressions
