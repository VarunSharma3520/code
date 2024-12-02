This cheatsheet covers the fundamental aspects of Go programming language.[official Go documentation](https://golang.org/doc/).

# golang cheatsheet

## basics

### hello world

```go
package main

import "fmt"

func main() {
    fmt.Println("Hello, World!")
}
```

### variables

```go
var x int
var y string
var z bool

x = 42
y = "Hello"
z = true

// Short-hand declaration
a := 10
b := "Go"
c := false
```

### constants

```go
const Pi = 3.14

const (
    Sunday = iota
    Monday
    Tuesday
)
```

### data types

```go
// basic types
var (
    a int
    b float64
    c bool
    d string
)

// composite types
var (
    e [5]int            // array
    f []int             // slice
    g map[string]int    // map
    h struct {          // struct
        x int
        y int
    }
    i *int              // pointer
    j func(int) int     // function
)
```

### functions

```go
func add(a int, b int) int {
    return a + b
}

// multiple return values
func swap(x, y string) (string, string) {
    return y, x
}

// named return values
func split(sum int) (x, y int) {
    x = sum * 4 / 9
    y = sum - x
    return
}
```

## control structures

### if-else

```go
if x > 0 {
    fmt.Println("x is positive")
} else if x < 0 {
    fmt.Println("x is negative")
} else {
    fmt.Println("x is zero")
}
```

### for loop

```go
// basic for loop
for i := 0; i < 10; i++ {
    fmt.Println(i)
}

// while-like loop
n := 0
for n < 5 {
    fmt.Println(n)
    n++
}

// infinite loop
for {
    // ...
}
```

### switch

```go
switch day {
case "Monday":
    fmt.Println("Start of the work week")
case "Friday":
    fmt.Println("Almost weekend!")
default:
    fmt.Println("Another day")
}
```

### defer

```go
defer fmt.Println("This will be printed last")

fmt.Println("First")
fmt.Println("Second")
```

## collections

### arrays

```go
var a [5]int
a[2] = 7
fmt.Println(a)
```

### slices

```go
s := []int{2, 3, 5, 7, 11, 13}
fmt.Println(s)

s = append(s, 17, 19)
fmt.Println(s)
```

### maps

```go
m := make(map[string]int)
m["route"] = 66
fmt.Println(m["route"])

delete(m, "route")
```

## structs

```go
type Vertex struct {
    X int
    Y int
}

v := Vertex{1, 2}
v.X = 4
```

### methods

```go
type Vertex struct {
    X, Y int
}

func (v Vertex) Abs() float64 {
    return math.Sqrt(v.X*v.X + v.Y*v.Y)
}

func (v *Vertex) Scale(f float64) {
    v.X = int(float64(v.X) * f)
    v.Y = int(float64(v.Y) * f)
}
```

### interfaces

```go
type Abser interface {
    Abs() float64
}

func describe(i Abser) {
    fmt.Printf("(%v, %T)\n", i, i)
}
```

## concurrency

### goroutines

```go
go func() {
    fmt.Println("In a goroutine")
}()
```

### channels

```go
ch := make(chan int)

go func() {
    ch <- 42
}()

fmt.Println(<-ch)
```

### select

```go
select {
case msg1 := <-ch1:
    fmt.Println("Received", msg1)
case msg2 := <-ch2:
    fmt.Println("Received", msg2)
default:
    fmt.Println("No message received")
}
```

## packages

### importing packages

```go
import (
    "fmt"
    "math"
    "time"
)
```

### creating packages

```go
// In file mypackage/mypackage.go
package mypackage

func MyFunction() {
    fmt.Println("Hello from mypackage")
}

// In main.go
package main

import "mypackage"

func main() {
    mypackage.MyFunction()
}
```

