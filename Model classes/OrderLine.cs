public class OrderLine
{
	public Order Order { get; set; }
	public Product Product { get; set; }
	public int Count { get; set; }
	public int Total { get; set; }

	public OrderLine(){}

	public OrderLine(Order order, Product product, int count, int total)
	{
		Order = order;
		Product = product;
		Count = count;
		Total = total;
	}
}
