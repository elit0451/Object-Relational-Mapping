public class Customer
{
	public string Name { get; set; }
	public List<Order> Orders { get; set; }

	public Customer(){}

	public Customer(string name, List<Order> orders)
	{
		Name = name;
		Orders = orders;
	}
}
