import useFetch from "./useFetch";


const Devices = () => {
    const url = "http://127.0.0.1:8000/xlease/items"
    const { data: items, loading, error } = useFetch(url);

    
    return ( 
        <section>
            <h2 className="devices-header">Devices</h2>
            { error && <div>{ error }</div> }
            { loading && <div>Loading...</div> }
            <div className="devices">
                { items && items.map((item) => {
                    return <div className="container" key={ item.id }>
                                <div className="photo-container">
                                    <img src={item.images[0].image} className="photo-container2" alt={ item.name }>
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