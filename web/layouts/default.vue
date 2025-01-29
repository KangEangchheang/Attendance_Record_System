<script setup lang="ts">
import { Home, Users, Contact, Book } from 'lucide-vue-next'

</script>

<template>
  <div class="bg-[#1c1c1c] text-white grid min-h-screen w-full md:grid-cols-[220px_1fr] lg:grid-cols-[280px_1fr]">
    <div class="hidden border-r border-r-white/10 bg-muted/40 md:block">
      <div class="flex h-full max-h-screen flex-col gap-2">
        <div class="flex h-14 items-center px-4 lg:h-[60px] lg:px-6">
          <span class="flex items-center gap-2 font-semibold">
            <Users class="h-6 w-6" />
            <span class="text-xl font-bold bg-gradient-to-r from-purple-400 via-pink-500 to-red-500 bg-clip-text text-transparent">Attendance System</span>
          </span>
        </div>
        <div class="flex-1">
          <nav class="grid text-slate-200 items-start px-2 text-base font-medium lg:px-4">
            <a href="/" class="flex items-center gap-3 rounded-lg px-3 py-2 font-semibold text-muted-foreground transition-all hover:text-primary hover:bg-white/10">
              <Home class="h-4 w-4" />
              Dashboard
            </a>

            <!-- <a href="/employee" class="flex items-center gap-3 rounded-lg px-3 py-2 font-semibold text-muted-foreground transition-all hover:text-primary hover:bg-white/10">
              <Contact class="h-4 w-4" />
              User
            </a> -->

            <a href="/about" class="flex items-center gap-3 rounded-lg px-3 py-2 font-semibold text-muted-foreground transition-all hover:text-primary hover:bg-white/10">
              <Book class="h-4 w-4" />
              About
            </a>
          </nav>
        </div>
        
      </div>
    </div>
    <main class="flex flex-1 flex-col bg-[#161616]">
      <NuxtPage/>
    </main>
  </div>
</template>