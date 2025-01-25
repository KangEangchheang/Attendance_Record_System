import { H3Event } from 'h3'
import sqlite3 from 'sqlite3';
import { open, Database } from 'sqlite';
import { writeFile, appendFile } from 'fs/promises';

let db: Database<sqlite3.Database, sqlite3.Statement> | null = null;

type QueryParams = {
    id?: number
    name?: string
}

export default defineEventHandler(async (event: H3Event) => {
  // Extract query parameters
  try {
    const query = getQuery<QueryParams>(event)

    // Validate query parameters
    const id = query.id || undefined
    const name = query.name || undefined

    if (!id || isNaN(id)) {
      throw createError({
        statusCode: 400,
        statusMessage: 'Invalid or missing "id" parameter',
      })
    }

    if (!name) {
      throw createError({
        statusCode: 400,
        statusMessage: 'Invalid or missing "time" parameter',
      })
    }
    
    // if (!db) {
    //   db = await open({
    //     filename: '../../database.sqlite', // Path to your SQLite database file
    //     driver: sqlite3.Database,
    //   });
    // }
    const status = 'present';


    // const queryStatement = `
    //   INSERT INTO employee (name, status)
    //   VALUES (?, ?);
    // `;

    // await db.run(queryStatement, [name, status]);

    // Ensure data is in CSV format
    const row = `${name},${Date.now()}\n`;

    try {
      // Append the row to 'attendance.csv'
      await appendFile('attendance.csv', row, 'utf8');
      console.log('Attendance logged successfully!');
    } catch (error) {
      console.error('Error writing to file:', error);
    }
      

    return {
      success: true,
      message: `Attendance log for employee with ID ${id} retrieved successfully`,
    }
  } catch (error: any) {
    throw createError({ statusCode: 400, message: error?.message })
  }
})
