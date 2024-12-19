# Write two methods with the same name but different number of parameters of same type 
and call the methods

# Class with method overloading using *args
class MyClass:
    def greet(self, *args):
        """Method to greet with different number of arguments."""
        if len(args) == 1:
            # If one argument, greet with just the name
            return f"Hello, {args[0]}!"
        elif len(args) == 2:
            # If two arguments, greet with name and occupation
            return f"Hello, {args[0]}! You are a {args[1]}."
        else:
            # Default case
            return "Hello, guest!"

# Create an instance of MyClass
obj = MyClass()

# Call the greet method with different numbers of arguments
print(obj.greet("Alice"))             
print(obj.greet("Bob", "Engineer"))   
print(obj.greet())



# Write two methods with the same name but different number of parameters of different 
data type and call the methods

public class MethodOverloadingExample {

    // Method with one parameter of type int
    public void display(int number) {
        System.out.println("The number is: " + number);
    }

    // Method with two parameters of type String and double
    public void display(String message, double value) {
        System.out.println(message + " " + value);
    }

    public static void main(String[] args) {
        MethodOverloadingExample example = new MethodOverloadingExample();

        // Call the method with an integer parameter
        example.display(42);

        // Call the method with a String and a double parameter
        example.display("The value is:", 99.99);
    }
}


# Write two methods with the same name and same number of parameters of same type  

public class MethodOverloadingError {
    // First method
    public void display(int number) {
        System.out.println("The number is: " + number);
    }

    // Second method with the same signature (causes an error)
    public void display(int value) {
        System.out.println("The value is: " + value);
    }

    public static void main(String[] args) {
        // This will cause a compilation error
    }
}
