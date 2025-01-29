import { readFile } from 'fs/promises';
import { defineEventHandler } from 'h3';

export default defineEventHandler(async () => {
    try {
        const filePath = 'attendance.csv'; // Ensure correct path
        const data = await readFile(filePath, 'utf8');
        const rows = data.split('\n').map(row => row.split(','));

        const attendance = rows.map(row => ({
            time: row[1]?.trim(),
            name: row[0]?.trim(),
        })).filter(row => row.name && row.time); // Remove empty rows

        return {
            success: true,
            message: 'Attendance data retrieved successfully',
            data: attendance
        };
    } catch (err) {
        console.error('Error reading CSV:', err);
        return {
            success: false,
            message: 'Failed to retrieve attendance logs',
            data: []
        };
    }
});
