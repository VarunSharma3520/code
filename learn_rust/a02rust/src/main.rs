#[derive(Debug)]
struct Rectangle {
    width: u32,
    height: u32,
}

fn area(rectangle: &Rectangle) -> u32 {
    rectangle.width * rectangle.height
}

fn main() {
    let rect1 = Rectangle {
        width: 30,
        height: 50,
    };
    dbg!(&rect1);

    println!("rect1: {:#?}", rect1);
    println!(
        "The area of the rectangle is {} square pixels.",
        area(&rect1)
    );

    let s1 = gives_ownership(); // gives_ownership moves its return
                                // value into s1

    let s2 = String::from("hello"); // s2 comes into scope

    println!("s2: {}", s2);
    let s3 = takes_and_gives_back(s2); // s2 is moved into
    println!("s3: {}", s3);
    println!("s1: {}", s1);
    let s4 = String::from("hello");
    first_word(&s4);
}

fn first_word(s: &String) -> usize {
    println!("{}", s);
    let bytes = s.as_bytes();
    for (i, &item) in bytes.iter().enumerate() {
        println!("{}", &item);
        if item == b' ' {
            return i;
        }
    }

    s.len()
}

fn gives_ownership() -> String {
    // gives_ownership will move its
    // return value into the function
    // that calls it

    let some_string = String::from("yours"); // some_string comes into scope

    some_string // some_string is returned and
                // moves out to the calling
                // function
}

// This function takes a String and returns one
fn takes_and_gives_back(a_string: String) -> String {
    // a_string comes into
    // scope

    a_string // a_string is returned and moves out to the calling function
}
