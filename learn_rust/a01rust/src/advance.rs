// struct
struct Employee {
  name: String,
  company: String,
  age: u32,
}

impl Employee {

  //static method that creates objects of the Point structure
  fn getInstance(x: i32, y: i32) -> Point {
    Point { x: x, y: y }
  }

  //display values of the structure's field
  fn display(&self) {
    println!("x ={} y={}", self.x, self.y);
  }
}

fn display(emp: Employee) {
  println!("Name is :{} company is {} age is {}",emp.name, emp.company, emp.age);
}

// enums
enum Color {
  Red,
  Green,
  Blue,
}

fn main() {
  println!("hi there everyone");
  let emp1 = Employee {
    company: String::from("TutorialsPoint"),
    name: String::from("Mohtashim"),
    age: 50,
  };

  let p1 = Point::getInstance(10, 20);
  p1.display();
  display(emp1);
}
