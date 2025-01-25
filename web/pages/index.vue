<script setup lang="ts">
import {
  createColumnHelper,
  FlexRender,
  getCoreRowModel,
  useVueTable,
} from '@tanstack/vue-table'
import { h, ref } from 'vue'

export interface Attendance {
  status: 'present' | 'late' | 'absent' 
  name: string
}

const data = ref<Attendance[]>([]);

onMounted(async ()=>{
  const { data: fetchData, status, error } = await useFetch<Attendance[]>('/api/log');
  data.value = fetchData.value || [];
  console.log(data.value)
})


const columnHelper = createColumnHelper<Attendance>()

const columns = [
  columnHelper.accessor('status', {
    enablePinning: true,
    header: 'Status',
    cell: ({ row }) => h('div', { class: 'capitalize' }, row.getValue('status')),
  }),
  columnHelper.accessor('name', {
    header: () => h('div', { class: 'text-left' }, 'Name'),
    cell: ({ row }) => h('div', { class: 'capitalize' }, row.getValue('name')),
  }),
]

const table = useVueTable({
  data,
  columns,
  getCoreRowModel: getCoreRowModel()
})
</script>

<template>
  <div class="w-full p-2">
    <!-- page title -->
    <div class="flex my-8 ml-4 items-center justify-between">
      <h1 class="text-3xl font-bold leading-tight tracking-tight text-white">
        Attendance
      </h1>
    </div>

    <Table>
      <TableHeader class="bg-white/5 rounded-xl">
        <TableRow v-for="headerGroup in table.getHeaderGroups()" :key="headerGroup.id">
          <TableHead v-for="header in headerGroup.headers" :key="header.id">
            <FlexRender v-if="!header.isPlaceholder" :render="header.column.columnDef.header" :props="header.getContext()" />
          </TableHead>
        </TableRow>
      </TableHeader>
      <TableBody>
        <template v-if="table.getRowModel().rows?.length">
          <TableRow v-for="row in table.getRowModel().rows" :key="row.id">
            <TableCell v-for="cell in row.getAllCells()" :key="cell.id">
              <FlexRender :render="cell.column.columnDef.cell" :props="cell.getContext()" />
            </TableCell>
            
          </TableRow>
        </template>

        <TableRow v-else>
          <TableCell :colspan="columns.length" class="h-24 text-center">
            No results.
          </TableCell>
        </TableRow>
      </TableBody>
    </Table>
    </div>
</template>