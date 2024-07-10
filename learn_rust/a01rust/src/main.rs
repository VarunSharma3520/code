

fn main() {
    println!("Hi,varun");
    let x: i8 = 4;
    let y: f32 = 4.6;
    let z: bool = true;
    let a: char = 'a';
    let b: u8 = 2;
    let c: &str = "varun";
    let d: String = String::from("Sharma");
    println!("{},{},{},{},{},{},{}",x,y,z,a,b,c,d);
    if z {
        println!("z = true");
    } else {
        println!("z = false");
    }
    if z && a == 'a' {
        println!("a = 'a' && z = true");
    } 
}
