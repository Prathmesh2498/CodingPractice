import java.util.Scanner;

public class Driver {
	final static String[] choices = { "1. PA", "2. TM", "3. TL", "4. ADMIN", "5. OTHERS" };
	final static Scanner sc = new Scanner(System.in);

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		Employee e = new Employee();
		System.out.println("Enter Name: ");
		String name = sc.next();
		System.out.println("Enter designation from following choices: ");
		for (String i:choices) {
			System.out.println(i);
		}
		int choice = sc.nextInt();
		String designation="";
		switch (choice) {
		case 1:
			designation = "PA";
			break;
		case 2:
			designation = "TM";
			break;
		case 3:
			designation = "TL";
			break;
		case 4:
			designation = "ADMIN";
			break;
		case 5:
			designation = "OTHERS";
			break;
		default:
			System.err.println("Enter Valid Choice!");
		}
		System.out.println("Enter Salary: ");
		int salary = sc.nextInt();
		
		e.setName(name);
		//Designation must be called before salary
		e.setDesignation(designation);
		e.setSalary(salary);
		e.diplay_info();

	}

}
