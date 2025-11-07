public class HelloWorld {
    public static void main(String[] args) {
        System.out.println("Hello, Java is working!");
        int[] arr={1,2,3,4,5};
        sumArray(arr);
        System.out.println("This is a simple Java program.");

        String str = "hello world";
        String upperStr = upperCae(str);
        System.out.println("Uppercase String: " + upperStr);

        int sum = sumVariable(1, 2, 3, 4, 5);
        System.out.println("Sum of variable arguments: " + sum);
    }

    public static void sumArray(int[] arr){
        int ans=0;
        for (int i=0;i<arr.length;i++){
            ans+=arr[i];
        }
        System.out.println("Sum of array elements: " + ans);
    }

    public static int sumVariable(int... numbers){
        int sum = 0;
        for (int number : numbers) {
            sum += number;
        }
        return sum;
    }

    public static String upperCae(String str){
        return str.toUpperCase();
    }
}
