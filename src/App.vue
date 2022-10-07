<template>
  <div id="app">
    <Header />
    <div class="board">
      <div class="lane">
        <h2 class="lane-title">Backlog</h2>
        <Container group-name="trello"
        @drag-start="dragStart('backlog', $event)" 
        @drop="dropStop('backlog', $event)" 
        :get-child-payload="getChildPayload"
        >
          <Draggable v-for="card in cards.backlog" :key="card.id">
            <Card>
              {{ card.text }}
            </Card>
          </Draggable>
        </Container>
      </div>
      <div class="lane">
        <h2 class="lane-title">Desenvolvimento</h2>
        <Container group-name="trello" 
        @drag-start="dragStart('desenvolvimento', $event)" 
        @drop="dropStop('desenvolvimento', $event)" 
        :get-child-payload="getChildPayload"
        >
          <Draggable v-for="card in cards.desenvolvimento" :key="card.id">
            <Card  draggable="true">
              {{ card.text }}
            </Card>
          </Draggable>
        </Container>
      </div>
      <div class="lane">
        <h2 class="lane-title">Testes</h2>
        <Container group-name="trello" 
        @drag-start="dragStart('testes', $event)"
        @drop="dropStop('testes', $event)" 
        :get-child-payload="getChildPayload"
        >
          <Draggable  v-for="card in cards.testes" :key="card.id">
            <Card>
              {{ card.text }}
            </Card>
          </Draggable>
        </Container>
      </div>
      <div class="lane">
        <h2 class="lane-title">Done</h2>
        <Container group-name="trello" 
        @drag-start="dragStart('done', $event)" 
        @drop="dropStop('done', $event)" 
        :get-child-payload="getChildPayload"
        >
          <Draggable v-for="card in cards.done" :key="card.id">
            <Card>
              {{ card.text }}
            </Card>
          </Draggable>
        </Container>
      </div>
    </div>
  </div>
</template>

<script>
import Header from './components/Header';
import Card from './components/Card.vue'
import initialCards  from './initialCards';
import  { Container, Draggable } from 'vue3-smooth-dnd'
export default {
  name: 'App',
  components: {
    Header,
    Card,
    Container,
    Draggable
  },
  data: () =>({
    newTask: '',
    cards: {
      backlog: initialCards.backlog,
      desenvolvimento: initialCards.desenvolvimento,
      testes: initialCards.testes,
      done: []
    },
    draggingCard: {
      lane: '',
      index: -1,
      cardData: {}
    },
  }),
  methods: {
    dragStart(lane, dragResult){
      const { payload, isSource } = dragResult
      if(isSource) {
        this.draggingCard = {
          lane,
          index: payload.index,
          cardData: {
            ...this.cards[lane][payload.index],
          },
        }
      }

    },
    dropStop(lane, dropResult){
      const { removedIndex, addedIndex } = dropResult
      if (lane === this.draggingCard.lane && removedIndex === addedIndex){
        return
      }
      if (removedIndex !== null){
        this.cards[lane].splice(removedIndex, 1)
      }
      if (addedIndex !== null){
        this.cards[lane].splice(addedIndex, 0, this.draggingCard.cardData)
      }
    },
    getChildPayload(index){
      return {
        index,
      }
    }, 
    addTask(){
      this.cards.push()
    }
  }
}
</script>

<style>
  .board {
    display: flex;
    justify-content: flex-start;
    flex-flow: wrap;
    align-items: flex-start;
    margin: 1.2rem;
  }

  .lane {
    width: 23rem;
    border-radius: .8rem;
    box-shadow: 0 .1rem .2rem 0 rgba(33, 33, 33, .1);
    background: var(--color-gray);
    margin: 0 .8rem;
  }

  .lane-title {
    width: 23rem;
    margin-bottom: .6rem;
    padding: .6rem;
    background: rgb(153, 153, 249);
    color: #fff;
    border-radius: .8rem .8rem 0 0;
  }
  
  @media (max-width:768px) {
    .lane {
      margin: 5rem 3rem;
    }
  }
</style>
