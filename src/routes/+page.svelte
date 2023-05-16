<script lang="ts">
    import { append } from "svelte/internal";

    interface TodoEntry {
        text: string
        completed: boolean
    }

    let todos: Array<TodoEntry> = []

    let inputValue = "";

    function addTodo(text: string) {
        todos.push({
            text: text,
            completed: false
        });
        todos = todos;
        inputValue = "";
    }

    $: console.log(todos)

    addTodo("test")
</script>


<h1 class="text-center text-3xl my-4">My Todo App</h1>

<main class="px-8">

    <div class="flex gap-2 my-2">
        <input bind:value={inputValue} type="text" placeholder="Add Todo" class="input basis-full input-bordered " />
        <button class="btn btn-success" on:click={() => addTodo(inputValue)}>Add</button>
    </div>

    <div class="overflow-x-auto">
        <table class="table w-full">
          <!-- head -->
          <thead>
            <tr>
                <th class="w-0"></th>
                <th class="w-0"></th>
                <th>Todo</th>
                <th class="w-0"></th>
            </tr>
          </thead>
          <tbody>
            {#each todos as todo, i}
                <tr>
                    <td class=""><input type="checkbox" class="checkbox align-middle" bind:checked={todo.completed}></td>
                    <td class="">{i+1}</td>
                    <td>{todo.text}</td>
                    <td><button on:click={() => {todos.splice(i, 1); todos = todos}} class="btn btn-error">Remove</button></td>
                </tr>
            {/each}
          </tbody>
        </table>
      </div>
</main>

