import { useEffect, useState } from "react";

const Devices = () => {
    let [items, setItem] = useState(null);
    let [error, setError] = useState(null);
    let [loading, setLoading] = useState(true);
    const url = "http://127.0.0.1:8000/xlease/items"

    useEffect(() => {
        fetch(url)
            .then(res => {
                if (!res.ok){
                    throw Error("Could not fetch data");
                }
                return res.json()
            }).then(data => {
                console.log(data);
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
        <section>
            <h2>Devices</h2>
            { error && <div>{ error }</div> }
            { loading && <div>Loading...</div> }
            <div className="devices">
                { items && items.map((item) => {
                    { console.log("Item obj =>", item.images[0].image);}
                    return <div className="container" key={ item.id }>
                                <div className="photo-container">
                                    <img src={item.images[0].image} className="photo-container2"  alt={ item.name }>
                                    </img>
                                </div>
                                <div className="name-price">
                                    <h4 >{ item.name }</h4>
                                    <h4>
                                        <b>${ item.price_per_day }</b>
                                    </h4>
                                </div>
                                <h5 className="description">{ item.description.slice(0,80) }...</h5>
                                <p className="categoty-tag">{ item.category }</p>
                                <button className="lease-device">
                                    Lease
                                </button>
                        </div>}
                )
                }
            </div>
         </section>
     )
}

export default Devices;