import { useParams } from "react-router-dom";
import useFetch from "./useFetch";
import { Link } from "react-router-dom";

const LeaseADevice = () => {
    const { id } = useParams();
    const { data: item, error, loading } = useFetch("http://127.0.0.1:8000/xlease/items/" + id);


    return ( 
        <div className="devices">
            { error && <div className="error">{ error }</div> }
            { loading && <div className="loading">Loading...</div> }
            { item && 
                <div className="container" key={ item.id }>
                    <div className="photo-container">
                        <img src={item.images[0].image} className="photo-container2" alt={ item.name }>
                        </img>
                    </div>
                    <div className="name-price">
                        <h4 >{ item.name }</h4>
                        <h4>
                            <b>${ item.price_per_day }/Month</b>
                        </h4>
                    </div>
                    <h5 className="description">{ item.description }...</h5>
                    <p className="categoty-tag">{ item.category }</p>
                    <Link to="#">
                        <button className="lease-device">Pay</button>
                    </Link>
                </div>
            }
        </div>
     );
}
 
export default LeaseADevice;