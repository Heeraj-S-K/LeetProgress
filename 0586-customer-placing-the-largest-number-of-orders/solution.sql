SELECT MAX(customer_number)
KEEP (DENSE_RANK LAST ORDER BY COUNT(order_number)) AS customer_number 
FROM Orders 
GROUP BY customer_number;

