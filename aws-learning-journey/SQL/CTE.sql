WITH DepartmentSalary AS (
    SELECT DepartmentID,
           AVG(Salary) AS AvgSalary
    FROM Employees
    GROUP BY DepartmentID
)
SELECT e.EmployeeName,
       e.Salary,
       d.AvgSalary
FROM Employees e
JOIN DepartmentSalary d
    ON e.DepartmentID = d.DepartmentID;
