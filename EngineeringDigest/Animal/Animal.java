
public class Animal {

    private String species;
    public String name;


    public void setSpecies(String species){
        this.species = species;
    }
    public String getSpecies() {
        return this.species;
    }
    public void sound() {
        System.out.println("The animal speaks");
    }
}
