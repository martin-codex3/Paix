<script lang="ts">
    import {page} from "$app/state";
    let { children } = $props();

    let toggleNavigation: boolean = $state(false);

    // we will control the navigation here
    const handleToggleNavigation = () => {
        toggleNavigation != toggleNavigation
    }
</script>

<main class="">
    <nav class=" {toggleNavigation ? 'hidden' : 'w-72 fixed'} main_navigation bg-stone-800 h-screen overflow-auto">
        <div class="site__logo py-2 px-4">
            <h1 class="font-extrabold text-2xl uppercase">paix</h1>
        </div>

        <div class="flex items-center justify-between px-4 py-4">
            <div>
                <h1>hey</h1>
            </div>

            <div>
                <button onclick="{handleToggleNavigation}" aria-label="button" class="flex items-center justify-center cursor-pointer">
                    <span class="icon-[tabler--menu-2] text-2xl"></span>
                </button>
            </div>
        </div>

        <div class="site__links px-2">
            <ul class="flex flex-col gap-2">
                <li>
                    <a href="/" class="flex items-center gap-2 w-full rounded-lg py-2
                     transition-all duration-150 ease-linear hover:bg-stone-500 px-2
                        {page.url.pathname === '/' ? 'bg-stone-500' : ''}">
                        <span class="icon-[tabler--home] text-xl"></span>
                        <span class="capitalize">home</span>
                    </a>
                </li>

                <li>
                    <a href="/file-manager" class="flex items-center gap-2 w-full rounded-lg py-2
                     transition-all duration-150 ease-linear hover:bg-stone-500 px-2
                        {page.url.pathname === '/file-manager' ? 'bg-stone-500' : ''}">
                        <span class="icon-[tabler--files] text-xl"></span>
                        <span class="capitalize">file manager</span>
                    </a>
                </li>

                <li>
                    <a href="/version-control" class="flex items-center gap-2 w-full rounded-lg py-2
                     transition-all duration-150 ease-linear hover:bg-stone-500 px-2
                        {page.url.pathname === '/version-control' ? 'bg-stone-500' : ''}">
                        <span class="icon-[tabler--versions] text-xl"></span>
                        <span class="capitalize">version control</span>
                    </a>
                </li>

                <li>
                    <a href="/structure" class="flex items-center gap-2 w-full rounded-lg py-2
                     transition-all duration-150 ease-linear hover:bg-stone-500 px-2
                        {page.url.pathname === '/structure' ? 'bg-stone-500' : ''}">
                        <span class="icon-[tabler--layout-grid-add] text-xl"></span>
                        <span class="capitalize">structure</span>
                    </a>
                </li>


                <li>
                    <a href="/security" class="flex items-center gap-2 w-full rounded-lg py-2
                     transition-all duration-150 ease-linear hover:bg-stone-500 px-2
                        {page.url.pathname === '/security' ? 'bg-stone-500' : ''}">
                        <span class="icon-[tabler--hand-stop] text-xl"></span>
                        <span class="capitalize">privacy and security</span>
                    </a>
                </li>

                <li>
                    <a href="/power" class="flex items-center gap-2 w-full rounded-lg py-2
                     transition-all duration-150 ease-linear hover:bg-stone-500 px-2
                        {page.url.pathname === '/power' ? 'bg-stone-500' : ''}">
                        <span class="icon-[tabler--battery-vertical-charging-2] text-xl"></span>
                        <span class="capitalize">power</span>
                    </a>
                </li>

                <li>
                    <a href="/appearance" class="flex items-center gap-2 w-full rounded-lg py-2
                     transition-all duration-150 ease-linear hover:bg-stone-500 px-2
                        {page.url.pathname === '/appearance' ? 'bg-stone-500' : ''}">
                        <span class="icon-[tabler--brush] text-xl"></span>
                        <span class="capitalize">appearance</span>
                    </a>
                </li>

                <li>
                    <a href="/settings" class="flex items-center gap-2 w-full rounded-lg py-2
                     transition-all duration-150 ease-linear hover:bg-stone-500 px-2
                        {page.url.pathname === '/settings' ? 'bg-stone-500' : ''}">
                        <span class="icon-[tabler--settings] text-xl"></span>
                        <span class="capitalize">settings</span>
                    </a>
                </li>

            </ul>
        </div>
    </nav>

    <div class="app_wrapper ml-72 px-5 pt-10">
        {@render children()}
    </div>
</main>