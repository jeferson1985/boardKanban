<template>
    <div class="card">
        <textarea></textarea>
        <slot></slot>
    </div>
</template>


<script>
export default {
    name: 'Card',
}
</script>

<style scoped>
    .card {
        background: var(--color-white);
        padding: 1.4rem;
        border-radius: .4rem;
        box-shadow: 0 1px 0 rgba(9, 30, 66, .25);
        margin-bottom: .8rem;
        cursor: pointer;
        font-size: 1.6rem;
    }
    textarea {
        width: 100%;
        border: 1px solid rgb(223, 222, 222);
        outline: 0;
    }
</style>