package inherit;

class Inheritance{
    public static void main(String[] args) {
        // Create an instance of the subclass

        Animal animal=new Animal();
        System.out.println("Hello, World!");
        animal.setSpecies("Dog");
        System.out.println("Animal species: " + animal.getSpecies());
        // animal.sound();  // Calls the overridden method from Dog class

        // Dog MyAnimal =(Dog)animal;
        // MyAnimal.bark();  // Calls the method from Dog class
        // System.out.println("MyAnimal species: " + MyAnimal.getSpecies());

        // dog.sound();  // Calls the overridden method from Dog class
      }


}

