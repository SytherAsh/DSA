class Test{
    public static void main(String[] args) {
        // Animal animal = new Animal();
        // System.out.println("Hello, World!");
        // animal.setSpecies("Dog");
        // System.out.println("Animal species: " + animal.getSpecies());
        // animal.name = "Buddy";
        // System.out.println("Animal name: " + animal.name);


        Cat cat= new Cat();
        cat.setSpecies("Cat");
        Cat a=makeCatbreed(cat);
        //! Both the objects are referring to the same object in memory
        System.out.println("Cat breed: " + cat.getSpecies());
        System.out.println("Cat species: " + a.getSpecies());

    }
    public static Cat makeCatbreed(Cat cat){
        cat.setSpecies("Siamese");
        return cat;
    }

}