<script setup lang="ts">
import { Home, Users } from 'lucide-vue-next'
</script>

<template>
  <div class="bg-[#151518] text-white grid min-h-screen w-full md:grid-cols-[220px_1fr] lg:grid-cols-[280px_1fr]">
    <div class="hidden border-r border-r-white/10 bg-muted/40 md:block">
      <div class="flex h-full max-h-screen flex-col gap-2">
        <div class="flex h-14 items-center border-b border-b-white/10 px-4 lg:h-[60px] lg:px-6">
          <span class="flex items-center gap-2 font-semibold">
            <Users class="h-6 w-6" />
            <span class="font-bold">Attendance System</span>
          </span>
        </div>
        <div class="flex-1">
          <nav class="grid text-slate-200/70 items-start px-2 text-base font-medium lg:px-4">
            <a href="/" class="flex items-center gap-3 rounded-lg px-3 py-2 font-semibold text-muted-foreground transition-all hover:text-primary hover:bg-white/5">
              <Home class="h-4 w-4" />
              Dashboard
            </a>
          </nav>
        </div>
        
      </div>
    </div>
    <div class="flex flex-col">
      <header class="flex h-14 items-center gap-4 border-b border-b-white/10 bg-muted/40 px-4 lg:h-[60px] lg:px-6">
        Admin
      </header>


      <main class="flex flex-1 flex-col gap-4 p-4 lg:gap-6 lg:p-6 bg-[#09090b]">
        <NuxtPage/>
      </main>
    </div>
  </div>
</template>