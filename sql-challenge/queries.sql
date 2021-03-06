-- List the following details of each employee: employee number, last name, first name, sex, and salary.


SELECT e.emp_no, e.first_name, e.last_name, e.sex, s.salary 
	FROM public.employees e
	inner join public.salaries s
	on e.emp_no=s.emp_no;
	
--List first name, last name, and hire date for employees who were hired in 1986.

SELECT e.first_name, e.last_name, e.hire_date
	FROM public.employees e
	where EXTRACT(YEAR FROM e.hire_date) = 1986;
--List the manager of each department with the following information: department number, department name, the manager's employee number, last name, first name

SELECT m.emp_no, m.dept_no, e.first_name, e.last_name, d.dept_name

from public.dept_manager m
inner join public.employees e
on e.emp_no=m.emp_no
inner join public.departments d
on  m.dept_no= d.dept_no;

--List the department of each employee with the following information: employee number, last name, first name, and department name.

SELECT e.emp_no, e.first_name, e.last_name, de.dept_no, d.dept_name
	FROM public.employees e
	inner join public.dept_emp de
	on e.emp_no=de.emp_no
	inner join public.departments d
	on de.dept_no=d.dept_no;
	
--List first name, last name, and sex for employees whose first name is "Hercules" and last names begin with "B."

SELECT e.first_name, e.last_name, e.sex 
	FROM public.employees e
	where e.first_name='Hercules' and e.last_name like 'B%';
	
-- List all employees in the Sales department, including their employee number, last name, first name, and department name.

SELECT e.emp_no, e.first_name, e.last_name, d.dept_name
	FROM public.employees e
	inner join public.dept_emp de
	on e.emp_no=de.emp_no
	inner join public.departments d
	on de.dept_no=d.dept_no
	
	where d.dept_name = 'Sales' ;
	
--Select * from public.departments;
--List all employees in the Sales and Development departments, including their employee number, last name, first name, and department name

SELECT e.emp_no, e.first_name, e.last_name, d.dept_name
	FROM public.employees e
	inner join public.dept_emp de
	on e.emp_no=de.emp_no
	inner join public.departments d
	on de.dept_no=d.dept_no
	
	where d.dept_name IN ('Sales', 'Development') ;

--In descending order, list the frequency count of employee last names, i.e., how many employees share each last name

SELECT e.last_name, count(e.last_name) as name_count
	FROM public.employees e
	
	group by e.last_name
	order by count(e.last_name) desc;
	
	----
	SELECT e.emp_no, count(e.emp_no) as Count_emp
	
	FROM public.employees e
	group by e.emp_no
	order by count(e.emp_no) desc;
------

ALTER TABLE dept_emp add Primary Key (emp_no, dept_no);

   
	

