public class Order
{
	public string Date { get; set; }
	public int Total { get; set; }
	public Customer Customer { get; set; }
	public List<OrderLine> Lines { get; set; }

	public Order(){}

	public Order(string date, int total, Customer customer, List<OrderLine> lines)
	{
		Date = date;
		Total = total;
		Customer = customer;
		Lines = lines;
	}
}
