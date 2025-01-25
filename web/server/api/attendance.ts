import { H3Event } from 'h3'
import sqlite3 from 'sqlite3';
import { open, Database } from 'sqlite';

let db: Database | null = null;

export default defineEventHandler(async(event: H3Event) => {
    if (!db) {
        db = await open({
        filename: '/database.sqlite',
        driver: sqlite3.Database,
        });
    }

    const Attendance = await db.all(`
        SELECT 
            attendance.*, 
            employee.name AS employee_name,
        FROM 
            attendance
        JOIN 
            amployee 
        ON 
            attendance.employee_id = employee.id;
    `);

    return {
        success: true,
        message: `Attendance logs retrieved successfully`,
        data: Attendance
    }
})
