import { useEffect, useState } from "react";
import { Link } from "react-router-dom";
import { useTranslation } from "react-i18next";



function BlogList() {
  const { t, i18n } = useTranslation();
  const [posts, setPosts] = useState([]);

  useEffect(() => {
    fetch(`/api/posts/?lang=${i18n.language}`)
      .then((response) => response.json())
      .then((data) => {
        setPosts(data);
      });
  }, [i18n.language]);

  return (
    <div>
      <h1>{t("blogList")}</h1>
      
      {posts.map((post) => (
        <div key={post.id}>
          <Link to={`/posts/${post.id}`}>
  <h2>{post.title}</h2>
</Link>

          <p>{post.summary}</p>
        </div>
      ))}
    </div>
  );
}

export default BlogList;