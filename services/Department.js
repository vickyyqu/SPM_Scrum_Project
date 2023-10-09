class DepartmentService{
    getAllDepartments(){

        let departments = ['CEO','Chairman','Sales','Solutioning','Engineering', 'HR', 'Finance', 'Consultancy', 'IT']
        return departments
    }
}

export default new DepartmentService()