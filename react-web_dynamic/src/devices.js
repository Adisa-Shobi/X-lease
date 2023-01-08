import { useEffect, useState } from "react";
import React from "react";

const Devices= () => {
  let [items, setItem] = useState([]);
  let [error, setError] = useState(null);
  let [loading, setLoading] = useState(true);
  const url = "http://127.0.0.1:8081/api/items"

  useEffect(() => {
    fetch(url)
      .then(res => {
        if (!res.ok){
          throw Error("Could not fetch data");
        }
        return res.json()
      }).then(data => {
        console.log(Object.getOwnPropertyNames(data));
        setItem(data);
	setLoading(false);
        console.log(loading);
        console.log("Items = ", items)
      }).catch(err => {
        console.log(err.message);
        setError(err.message);
      })
  }, []);
  return (
      <section className="devices">
      <h2 className="section-header">Devices</h2>
      { error && <div>{ error }</div> }
    { loading && <div>Loading...</div> }
    { console.log("Itemj: ", items) }
    { items && items.map((item) => {
      return (
	// item.name.replace(/ /g, "-").toLowerCase()
	  <article className="device">
	  <div className="photo-container">
          <img src={ item.img_src } className="device-photo"  alt={ item.name }>
          </img>
          </div>
          <div className="name-price">
          <h4 className="name">{ item.name }</h4>
          <h4 className="price">
          <b>${ item.price_per_day }</b>
          </h4>
          </div>
          <h5 className="description">{ item.description.slice(0 ,80) }...</h5>
          <p className="categoty-tag">{ item.category }</p>
          <button className="lease-device">
          Lease
	</button>
          </article>)
    }
			)}
    </section>
  )
}

export default Devices;
