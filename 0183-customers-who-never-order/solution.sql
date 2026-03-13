SELECT name as Customers
from Customers
WHERE id NOT IN (
    SELECT CustomerId
    from Orders
);
