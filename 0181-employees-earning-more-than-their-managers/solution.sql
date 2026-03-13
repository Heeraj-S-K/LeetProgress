SELECT e.name as Employee
FROM Employee e where e.salary >(
    Select m.salary
    FRoM Employee m
    where m.id = e.managerId
)
