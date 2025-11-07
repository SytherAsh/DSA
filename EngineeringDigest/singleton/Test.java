package singleton;
import inherit.Animal;

class Test{
    public static void main(String[] args){
        Animal animal = new Animal();
        animal.setSpecies("Dog");
        System.out.println("Animal species: " + animal.getSpecies());
        animal.sound();  // Calls the method from Animal class
        System.out.println("Animal sound: ");

        System.out.println("Hello, World!");

        // School school1 = School.getInstance();
        // School school2 = School.getInstance();
        // school1.display();
    }
}
class School{

    private static School instance;

    private School() {
        // Private constructor to prevent instantiation
    }
    public static School getInstance() {
        //! Singleton Pattern
        if (instance == null) {

            instance = new School();
        }else{
            System.out.println("Instance already created, returning existing instance.");
        }
        return instance;
    }
}
