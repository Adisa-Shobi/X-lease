import useFetch from "./useFetch";
import { Link } from "react-router-dom";

const Devices = () => {
  const url = "http://127.0.0.1:8081/api/items"
  const { data: items, loading, error } = useFetch(url);

  return (
      <section className="devices">
      <h2 className="devices-header">Devices</h2>
      { error && <div className="error">{ error }</div> }
    { loading && <div className="loading">Loading...</div> }
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
	  <Link to={ "lease-a-device/" + item.id }>
	  <button className="lease-device">
	  Lease
	</button>
	  </Link>
	  </article>
      )
    }
			)
    }
    </section>
  )
}
export default Devices;
