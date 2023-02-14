import React from "react";

function Cards(props) {
  const { cards } = props;
  console.log(cards);
  return (
    <div className="cards-container">
      {cards.map((card, key) => (
        <div className="cards" key={key}>
          <button
            className="card-img"
            style={{
              backgroundImage: `url(https://deckofcardsapi.com/static/img/${card}.png)`,
            }}
          ></button>
        </div>
      ))}
      {/* <div className="cards">
        <button
          className="card-img"
          style={{
            backgroundImage: `url(https://deckofcardsapi.com/static/img/5S.png)`,
          }}
        ></button>
      </div>
      <div className="cards">
        <button
          className="card-img"
          style={{
            backgroundImage: `url(https://deckofcardsapi.com/static/img/5S.png)`,
          }}
        ></button>
      </div>
      <div className="cards">
        <button
          className="card-img"
          style={{
            backgroundImage: `url(https://deckofcardsapi.com/static/img/5S.png)`,
          }}
        ></button>
      </div>
      <div className="cards">
        <button
          className="card-img"
          style={{
            backgroundImage: `url(https://deckofcardsapi.com/static/img/5S.png)`,
          }}
        ></button>
      </div>
      <div className="cards">
        <button
          className="card-img"
          style={{
            backgroundImage: `url(https://deckofcardsapi.com/static/img/5S.png)`,
          }}
        ></button>
      </div>
      <div className="cards">
        <button
          className="card-img"
          style={{
            backgroundImage: `url(https://deckofcardsapi.com/static/img/5S.png)`,
          }}
        ></button>
      </div>
      <div className="cards">
        <button
          className="card-img"
          style={{
            backgroundImage: `url(https://deckofcardsapi.com/static/img/5S.png)`,
          }}
        ></button>
      </div>
      <div className="cards">
        <button
          className="card-img"
          style={{
            backgroundImage: `url(https://deckofcardsapi.com/static/img/5S.png)`,
          }}
        ></button>
      </div>
      <div className="cards">
        <button
          className="card-img"
          style={{
            backgroundImage: `url(https://deckofcardsapi.com/static/img/5S.png)`,
          }}
        ></button>
      </div>
      <div className="cards">
        <button
          className="card-img"
          style={{
            backgroundImage: `url(https://deckofcardsapi.com/static/img/5S.png)`,
          }}
        ></button>
      </div> */}
      {/* <div className="cards">tets</div>
      <div className="cards">tets</div>
      <div className="cards">tets</div>
      <div className="cards">tets</div> */}
    </div>
  );
}

export default Cards;
