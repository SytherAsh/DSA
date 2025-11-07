

public class Animal {
    private String species; 
    protected String sound;

    public Animal(String species, String sound) {
        this.species = species;
        this.sound = sound;
    }

    public void setSpecies(String species) {
        this.species = species;
    }

    public String getSpecies() {
        return this.species;
    }
    public void sound() {
        System.out.println("The animal makes a sound " + this.sound);
    }

    protected void changesound(String newSound) {
        this.sound = newSound;
    }
}

class Dog extends Animal {
    public Dog () {
        super("Dog", "Bark");
    }
    String breed;

    public void bark() {
        System.out.println("Woof! Woof!");
    }

    public void setsound(String newsound){
        changesound(newsound);
    }
}


class puppy extends Dog {
    public void sound() {
        System.out.println("The puppy yips");
    }

    public void play() {
        System.out.println("The puppy plays with a ball");
    }
}