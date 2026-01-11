<script lang="ts">
    let { children } = $props();

    // we will control
</script>

<main class="">
    <nav class="fixed w-72 main_navigation bg-stone-800 h-screen overflow-auto">
        <div class="site__logo py-2 px-4">
            <h1 class="font-extrabold text-2xl uppercase">paix</h1>
        </div>

        <div class="site__links px-2">
            <ul class="flex flex-col gap-3">
                <li>
                    <a href="/" class="flex items-center gap-2 w-full rounded-lg py-2
                     transition-all duration-150 ease-linear hover:bg-stone-500 px-2">
                        <span class="icon-[tabler--home] text-xl"></span>
                        <span class="capitalize">home</span>
                    </a>
                </li>

                <li>
                    <a href="/" class="flex items-center gap-2 w-full rounded-lg py-2
                     transition-all duration-150 ease-linear hover:bg-stone-500 px-2">
                        <span class="icon-[tabler--files] text-xl"></span>
                        <span class="capitalize">file manager</span>
                    </a>
                </li>

                <li>
                    <a href="/" class="flex items-center gap-2 w-full rounded-lg py-2
                     transition-all duration-150 ease-linear hover:bg-stone-500 px-2">
                        <span class="icon-[tabler--versions] text-xl"></span>
                        <span class="capitalize">version control</span>
                    </a>
                </li>

                <li>
                    <a href="/" class="flex items-center gap-2 w-full rounded-lg py-2
                     transition-all duration-150 ease-linear hover:bg-stone-500 px-2">
                        <span class="icon-[tabler--layout-grid-add] text-xl"></span>
                        <span class="capitalize">structure</span>
                    </a>
                </li>


                <li>
                    <a href="/" class="flex items-center gap-2 w-full rounded-lg py-2
                     transition-all duration-150 ease-linear hover:bg-stone-500 px-2">
                        <span class="icon-[tabler--hand-stop] text-xl"></span>
                        <span class="capitalize">privacy and security</span>
                    </a>
                </li>

                <li>
                    <a href="/" class="flex items-center gap-2 w-full rounded-lg py-2
                     transition-all duration-150 ease-linear hover:bg-stone-500 px-2">
                        <span class="icon-[tabler--battery-vertical-charging-2] text-xl"></span>
                        <span class="capitalize">power</span>
                    </a>
                </li>

                <li>
                    <a href="/" class="flex items-center gap-2 w-full rounded-lg py-2
                     transition-all duration-150 ease-linear hover:bg-stone-500 px-2">
                        <span class="icon-[tabler--brush] text-xl"></span>
                        <span class="capitalize">appearance</span>
                    </a>
                </li>

                <li>
                    <a href="/" class="flex items-center gap-2 w-full rounded-lg py-2
                     transition-all duration-150 ease-linear hover:bg-stone-500 px-2">
                        <span class="icon-[tabler--settings] text-xl"></span>
                        <span class="capitalize">settings</span>
                    </a>
                </li>

            </ul>
        </div>
    </nav>

    <div class="app_wrapper ml-72">
        {@render children()}
    </div>
</main>