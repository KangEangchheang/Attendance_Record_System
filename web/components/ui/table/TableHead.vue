<script setup lang="ts">
import type { HTMLAttributes } from 'vue'
import { cn } from '@/lib/utils'

const props = defineProps<{
  class?: HTMLAttributes['class']
}>()
</script>

<template>
  <th :class="cn('h-12 px-4 text-left align-middle font-medium text-white/90 [&:has([role=checkbox])]:pr-0 dark:text-white', props.class)">
    <slot />
  </th>
</template>
