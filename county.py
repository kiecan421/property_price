class County:

  def __init__(self, n: str, new, resale, num_sales, avg) -> None:
      self.name = n
      self.new_house_pct = new
      self.resale_pct = resale
      self.number_of_sales = num_sales
      self.average_price = avg