import 'dart:io';

// Interface
abstract class Animal {
  void makeSound();
}

// Base class
class LivingBeing {
  void breathe() {
    print("I am breathing...");
  }
}

// Class that implements an interface
class Dog extends LivingBeing implements Animal {
  @override
  void makeSound() {
    print("Woof Woof!");
  }
}

// Class that overrides an inherited method
class Cat extends LivingBeing implements Animal {
  @override
  void makeSound() {
    print("Meow Meow!");
  }
}

// Class to initialize data from a file
class FileReader {
  List<String> readDataFromFile(String fileName) {
    File file = File(fileName);
    List<String> lines = file.readAsLinesSync();
    return lines;
  }
}

// Method demonstrating the use of a loop
void printList(List<String> list) {
  for (String item in list) {
    print(item);
  }
}

void main() {
  // Creating instances of classes
  Dog dog = Dog();
  Cat cat = Cat();
  FileReader fileReader = FileReader();

  // Using methods and properties
  dog.breathe();
  dog.makeSound();

  cat.breathe();
  cat.makeSound();

  // Initializing data from a file
  List<String> dataFromFile = fileReader.readDataFromFile("data.txt");

  // Using a loop
  printList(dataFromFile);
}

