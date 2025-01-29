<template>
  <div class="w-full p-4">
    <!-- Page Title -->
    <div class="flex my-6 items-center justify-between">
      <h1 class="text-3xl font-bold text-gray-200">Attendance</h1>
    </div>

    <!-- Table -->
    <div class="overflow-x-auto bg-gray-800 shadow-lg rounded-lg">
      <table class="min-w-full border border-gray-700 text-gray-300">
        <thead class="bg-gray-700 text-gray-200">
          <tr>
            <th class="py-3 px-4 text-left">Time</th>
            <th class="py-3 px-4 text-left">Name</th>
          </tr>
        </thead>
        <tbody>
          <tr v-for="(item, index) in attendance" :key="index" class="border-b border-gray-700 hover:bg-gray-700">
            <td class="py-3 px-4">{{ item.time }}</td>
            <td class="py-3 px-4">{{ item.name }}</td>
          </tr>
        </tbody>
      </table>
    </div>
  </div>
</template>

<script setup lang="ts">
const { data: attendance } = await useAsyncData('attendance', async () => {
  const response = await fetch('/api/attendance');
  const json = await response.json();
  return json.data; // Ensure we're accessing the correct property
});
onMounted(() => {
  refreshNuxtData('attendance');
})
</script>

<style scoped>
/* No additional styles needed since Tailwind is used */
</style>
