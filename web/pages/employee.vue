<script lang="ts" setup>

</script>

<template>
    <div class="w-full p-4">
         <Dialog>
            <DialogTrigger>
                <button type="button" class="font-semibold text-white bg-gradient-to-r from-red-400 via-red-500 to-red-600 hover:bg-gradient-to-br focus:ring-4 focus:outline-none focus:ring-red-300 dark:focus:ring-red-800 shadow-lg shadow-red-500/50 dark:shadow-lg dark:shadow-red-800/80 rounded-lg text-sm px-5 py-2.5 text-center me-2 mb-2">
                    Create User
                </button>
            </DialogTrigger>
            <DialogContent>
            <DialogHeader>
                <DialogTitle>Edit profile</DialogTitle>
                <DialogDescription>
                Make changes to your profile here. Click save when you're done.
                </DialogDescription>
            </DialogHeader>

            <DialogFooter>
                Save changes
            </DialogFooter>
            </DialogContent>
        </Dialog>
    </div>
</template>
