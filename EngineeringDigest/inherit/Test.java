class Test{
public static void main(String[] args) {

        Dog dog = new Dog();
        dog.sound();  // Calls the overridden method from Dog class
        dog.setsound("Woof Woof");
        dog.sound();  // Calls the overridden method from Dog class
        dog.bark();  // Calls the method from Dog class
        //!Upcasting
        // Animal animal=new Dog();
        // System.out.println("Hello, World!");
        // animal.setSpecies("Dog");
        // System.out.println("Animal species: " + animal.getSpecies());
        // animal.sound();  // Calls the overridden method from Dog class

        //!Downcasting
        // Dog MyAnimal =(Dog)animal;
        // MyAnimal.bark();  // Calls the method from Dog class
        // System.out.println("MyAnimal species: " + MyAnimal.getSpecies());

        // // Dog dog = new Dog();
        // // dog.sound();  // Calls the overridden method from Dog class
      }
}