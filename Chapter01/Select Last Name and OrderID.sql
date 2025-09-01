USE hplussport;
SELECT LastName,
    OrderId
FROM Customer
    JOIN Orders ON Customer.CustomerId = Orders.CustomerId