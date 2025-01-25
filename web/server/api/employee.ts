import { defineEventHandler, readMultipartFormData, createError, H3Event } from 'h3'
import sqlite3 from 'sqlite3';
import { open, Database } from 'sqlite';
import { useFetch } from 'nuxt/app';

let db: Database | null = null;

const MAX_FILE_SIZE = 5 * 1024 * 1024; // 5MB

export default defineEventHandler(async(event: H3Event) => {
    const method = event.node.req.method;
    

    if (!db) {
        db = await open({
        filename: '/database.sqlite',
        driver: sqlite3.Database,
        });
    }

    if (method === 'POST') { 
        //reading and validating the form
        const body = await readMultipartFormData(event);
        if (!body || body.length === 0) {
            throw createError({ statusCode: 400, message: 'No data uploaded.' });
        }

        
        let files;
        let name;
        for (const field of body) {
            if (field.name === 'name') {
                name = field.data.toString('utf-8');;
            } else if (field.name === 'file') {
                files = field;
            }
        }

        if (!files) {
            throw createError({ statusCode: 400, message: 'No file uploaded.' });
        }
        // Validate file size
        if (files.data.length > MAX_FILE_SIZE) {
            throw createError({ statusCode: 400, message: 'File size exceeds the limit of 5MB.' });
        }

        const queryStatement = `
        INSERT INTO employee (name)
        VALUES (?);
        `;

        const result = await db.run(queryStatement, [name]);


        const formdata = new FormData();
        if (files && files.data) {
            const blob = new Blob([files.data], { type: files.type || 'application/octet-stream' });
                formdata.append('file', blob, files.filename); // Append the Blob to FormData
            }
        formdata.append('custom_filename', `${result.lastID}_${name}`);


        const res = await fetch('http://localhost:5000/upload', {
            method: 'POST',
            body: formdata, // Pass the FormData object directly
        }).catch((error) => {
            console.log(error)
            throw createError({ statusCode: 400, message: 'File cannot upload try again' });
        });




        return {
            success: true,
            message: `Employees created successfully`,
        }
    }

    if (method === 'GET') {
    
        const result = await db.all(`SELECT * FROM employee`);

        return {
            success: true,
            message: `Employees retrieved successfully`,
            data: result
        }

    }
})
