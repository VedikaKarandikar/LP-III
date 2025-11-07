// SPDX-License-Identifier:MIT
pragma solidity ^0.8.0;

contract EmployeeDetails{
    struct Employee{
        uint id;
        string name;
        uint salary;
        string joiningDate;
    }
    Employee[] public employee;

    function createEmployee(uint _id, string memory _name, uint _salary, string memory _joiningDate) public{
        employee.push(Employee(_id,_name,_salary,_joiningDate));
    }
    function getEmployeeDetails(uint256 index) public view returns(uint, string memory, uint, string memory){
        require (index<employee.length, "Employee not found");
        return (employee[index].id, employee[index].name,employee[index].salary,employee[index].joiningDate);
    }

}
