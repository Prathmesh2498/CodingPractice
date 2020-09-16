
public class Employee {
	private String name, designation;
	private double salary, allowance, gross_salary;
	private double net_salary;
	

	public String getName() {
		return name;
	}

	public void setName(String name) {
		this.name = name;
	}

	public double getSalary() {
		return salary;
	}

	public void setSalary(int salary) {
		this.salary = salary;
		calculate_allowance();
		calculateTaxes();
	}

	public double getAllowance() {
		return allowance;
	}

	public void setAllowance(int allowance) {
		this.allowance = allowance;
	}

	public double getNet_salary() {
		return net_salary;
	}

	public void setNet_salary(double sal) {
		this.net_salary = sal;
	}

	public double getGross_salary() {
		return gross_salary;
	}

	public void setGross_salary(double gross_salary) {
		this.gross_salary = gross_salary;
	}

	public String getDesignation() {
		return designation;
	}

	public void setDesignation(String designation) {
		this.designation = designation;
		
	}
	
	
	private void calculateTaxes() {
		double sal = getSalary();
		if (sal>20000) {
			sal = getGross_salary() - ((13*getGross_salary())/100);
			setNet_salary(sal);
		}
		else if (15000<=sal && sal<=20000) {
			sal = getGross_salary() - ((12.5*getGross_salary())/100);
			setNet_salary(sal);
		}
		else if (12500<=sal && sal<=14999) {
			sal = getGross_salary() - ((11.5*getGross_salary())/100);
			setNet_salary(sal);
		}
		else if (7500<=sal && sal<=12499) {
			sal = getGross_salary() - ((12.5*getGross_salary())/100);
			setNet_salary(sal);
		}
		else {
			setNet_salary(getGross_salary());
		}
	}

	private void calculate_allowance() {
		String s = getDesignation();
		switch (s) {
		case ("PA"):
			setAllowance(1600);
			setGross_salary(getSalary()+1600);
			break;
		case ("TM"):
			setAllowance(1300);
			setGross_salary(getSalary() + 1300);
			break;
		case ("TL"):
			setAllowance(1270);
			setGross_salary(getSalary() + 1270);
			break;
		case ("ADMIN"):
			setAllowance(1500);
			setGross_salary(getSalary() + 1500);
			break;
		case ("OTHERS"):
			setAllowance(1100);
			setGross_salary(getSalary() + 1100);
			break;
		default:
			setAllowance(0);

		}
	}
	
	public void diplay_info() {
		System.out.println("Name: "+getName());
		System.out.println("Designation: "+getDesignation());
		System.out.println("Basic Salary: "+getSalary());
		System.out.println("Gross Salary: "+getGross_salary());
		System.out.println("Salary after Taxes: "+getNet_salary());
	}
	

}
