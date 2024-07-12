// https://projects.100xdevs.com/tracks/rust-bootcamp/Rust-Bootcamp-1
// Harkirat Singh YouTube Channel

use std::fs::File;

struct Rect {
    width: u32,
    height: u32,
}

impl Rect {
    fn area(&self) -> u32 {
        self.width * self.height
    }
}

fn main() {
    println!("Hi,varun");
    
    let x: i8 = 4;
    let y: f32 = 4.6;

    let z: bool = true;
    let a: char = 'a';
    let b: u8 = 2;

    let c: &str = "varun";
    let d: String = String::from("Sharma");

    println!("{},{},{},{},{},{},{}", x, y, z, a, b, c, d);
    let is_even = is_even(x);
    if is_even {
        print!("{} is even", x);
    } else {
        print!("{} is odd", x);
    }

    let rect = Rect {
        width: 30,
        height: 50,
    };
    print!("The area of the rectangle is {}", rect.area());

    let f = File::open("main.jpg");   // main.jpg doesn't exist
    match f {
        Ok(f)=> {
            println!("Entered in OK");
            println!("file found {:?}",f);
        },
        Err(e)=> {
            println!("Entered in ERR");
            println!("file not found \n{:?}",e);   //handled error
        }
    }


    // Memory Management
    mutability();
    heap_and_mutability();
    ownership();
    borrowing();
}

// defining a public function
pub fn is_even(x: i8) -> bool {
    return x % 2 == 0;
}

// Memory management is a crucial aspect of programming in Rust, designed to ensure safety and efficiency without the need for a garbage collector. 
// Not having a garbage collector is one of the key reasons rust is so fast
// It achieves this using the
// 1. Mutability
// 2. Heap and memory
// 3. Ownership model
// 4. Borrowing and references

fn mutability() {
    // let x: i32 = 1;
    // x = 2; // Error because x is immutable
    // println!("{}", x);

    let mut e: i8 = 1;
    println!("{}", e);
    e = 2; // No error
    println!("{}", e);
}


fn heap_and_mutability() {
    stack_fn();   // Call the function that uses stack memory
    heap_fn();    // Call the function that uses heap memory
    update_string();  // Call the function that changes size of variable at runtime
}

fn stack_fn() {
    // Declare a few integers on the stack
    let a = 10;
    let b = 20;
    let c = a + b;
    println!("Stack function: The sum of {} and {} is {}", a, b, c);
}

fn heap_fn() {
    // Create a string, which is allocated on the heap
    let s1 = String::from("heap_fn");
    let s2 = String::from("World");
    let combined = format!("{} {}", s1, s2);
    println!("Heap function: Combined string is '{}'", combined);
}

fn update_string() {
    // Start with a base string on the heap
    let mut s = String::from("update_string");
    println!("Before update: {}", s);

    // Append some text to the string
    s.push_str(" and some additional text");
    println!("After update: {}", s);
}

fn ownership() {
    // let s1 = String::from("hello");
    // let s2 = s1;
    // println!("{}", s1); // This line would cause a compile error because ownership has been moved.

    let s1 = String::from("ownership");
    let s2 = s1.clone();
    println!("value of s1:{}", s1); // Compiles now
    println!("value of s2:{}", s2); // Compiles now
    
}
fn borrowing() {
    let s1 = String::from("borrowing");
    let s2 = &s1;

    println!("{}", s1);    // This is valid
    println!("{}", s2);
    println!("{}", s1);    // This is valid, The first pointer wasn't invalidated
}
