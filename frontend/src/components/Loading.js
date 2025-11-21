import { Spinner } from "react-bootstrap";

function Loading() {
    return (
        <div className="d-flex justify-content-center align-items-center" style={{ height: "70vh" }}>
            <Spinner animation="border" role="status" variant="primary">
                <span className="visually-hidden">Loading...</span>
            </Spinner>
        </div>
    );
}

export default Loading;