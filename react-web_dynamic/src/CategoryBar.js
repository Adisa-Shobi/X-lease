
const CategoryBar = () => {
    let categories = ['Gaming', 'Filming', 'Recording', 'Mobile', 'Computer', 'Audio', 'Wearables', 'Fitness', 'PA systems']

    const categoryName = "b"
    return ( 
        <div id="categories">
            {categories.map((category) => (
                <button className="category" key={ category }>
                    <div className="icon"></div>
                    <p className="tag">{ category }</p>
                </button>
            ))}
            

        </div>
     );
}
 
export default CategoryBar;